from ..exceptions import except_orm
from .orm import AbstractModel, Model, TransientModel

except_osv = except_orm
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel
