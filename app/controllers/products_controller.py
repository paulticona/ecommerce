from app import db
from app.models.products_model import ProductModel
from app.schemas.products_schema import ProductsResponseSchema
from app.utils.bucket import Bucket


class ProductsController:
    def __init__(self):
        self.model = ProductModel
        self.schema = ProductsResponseSchema
        self.bucket = Bucket('paul-backend', 'products')

        self.__allowed_extensions = ['jpg', 'png', 'jpeg', 'webp']

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
                'message': 'NO se encontro el Producto mencionado'
            }, 404

        except Exception as e:
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            filename, stream = self.__validateExtencionImage(data['image'])
            image_url = self.bucket.uploadObject(stream, filename)
            data['image'] = image_url
            # image_url es la construccion de una url directa a la imagen requerida
            print(image_url)
            # data contiene toda la infomacion del producto
            print(data)
            # print(data['image'].__dict__)
            # key=valuye key=value1 ...key=valuen
            new_record = self.model.create(**data)
            # * agregamos la data a la DB mediente la conneccion
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)
            return {
                'message': 'El Producto se creo con exito',
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
                # validamos que haya una imagen para actualizar
                if data['image']:
                    filename, stream = self.__validateExtencionImage(data['image'])
                    image_url = self.bucket.uploadObject(stream, filename)
                    data['image'] = image_url

                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'message': 'El Producto se actulizo con exito',
                    'data': response.dump(record),
                }, 200

            return {
                'message': 'NO se encontro el Producto mecionado'
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
                    'message': 'Se desabilito el Producto con exito'
                }

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Orcurrio un error',
                'error': str(e)
            }, 500

    def __validateExtencionImage(self, image):
        filename = image.filename
        stream = image.stream
        # nombre_achivo.extencion el indice 1
        extencion = filename.split('.')[1]
        if extencion not in self.__allowed_extensions:
            raise Exception('El tipo de archivo usado no esta permitido')

        return filename, stream
