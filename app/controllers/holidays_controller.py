
from app import db
from app.models.holidays_model import HolidayModel
from app.schemas.holidays_schema import HolidaysResponseSchema, HolidaysDeliveryResponseSchema
from datetime import datetime, timedelta
from pytz import timezone
from locale import setlocale, LC_ALL


class HolidaysController:
    def __init__(self):
        self.model = HolidayModel
        self.schema = HolidaysResponseSchema
        self.schema_delivery = HolidaysDeliveryResponseSchema

        self.__max_count = 5
        self.__start_hour = '00:00:00'
        self.__end_hour = '21:00:00'
        self.__not_working = [6]  # 0-lUnes... 6-domingo

        self.timezone = timezone('America/Lima')
        self.datetimenow = datetime.now(tz=self.timezone)
        self.hournow = self.datetimenow.strftime('%H:%M:%S')
        setlocale(LC_ALL, 'es_ES')

    def all(self):
        try:
            records = self.model.where(status=True).order_by('id').all()
            response = self.schema(many=True)

            return {
                'data': response.dump(records)
            }
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro el Feriado mencionado'
            }, 404

        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def deliveryDates(self):
        try:
            records = self.model.where(status=True).order_by('date').all()
            holidays = [
                datetime.strftime(holiday.date, '%d-%#m')
                for holiday in records
            ]

            date_now = self.datetimenow.date()

            if self.hournow > self.__end_hour or self.hournow < self.__start_hour:
                date_now += timedelta(days=1)

            delivery_dates = []
            count = 0
            while count < self.__max_count:
                date_now += timedelta(days=1)

                if date_now.weekday() not in self.__not_working:
                    if f'{date_now.day}-{date_now.month}' not in holidays:
                        delivery_dates.append(
                            {
                                'date': date_now,
                                'format': datetime.strftime(
                                    date_now, '%A, %d de %B'
                                )
                            }
                        )
                        count += 1

            response = self.schema_delivery(many=True)
            return {
                'data': response.dump(delivery_dates)
            }, 200
        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:

            # key=valuye key=value1 ...key=valuen
            new_record = self.model.create(**data)
            # * agregamos la data a la DB mediente la conneccion
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)
            return {
                'message': 'el1 Feriado se creo con exito',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            #! 1:26 video
            # UPDATE roles SET field=value WHERE id = ?
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'message': 'El Feriado se actulizo con exito',
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro el Feriado mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():

                if record.status:
                    record.update(status=False)
                    db.session.add(record)
                    db.session.commit()
                return {
                    'message': 'Se desabilito el Feriado con exito'
                }

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500
