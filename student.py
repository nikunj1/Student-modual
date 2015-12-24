from openerp.osv import  osv,fields
from datetime import datetime 
from datetime import timedelta
import time

class  res_student(osv.osv):
    _name="res.student"

    
    
    def _total_num(self,cr,uid,ids,field,arg,context=None):
        res = {}
        print ids
        for record in self.browse(cr,uid,ids):
            res[record.id] = record.num1 + record.num2
            print res
        return res
     
    def _sum_total(self,cr,uid,ids,field,arg,context=None):
        res = {}
        total = 0.0
      #  print ids,ids[0]
        
        total = total + 10
            
        #res[ids[0]] = total
        res[ids[0]] = {
                       'sum' : total,
                       'sum1' : 50
                      }
        print res
        print 'ok' 
        return res
     
    
    _columns = {
                    'name': fields.char("Student Name"),
                    'class_id': fields.many2one('res.class',"Student Class" ),
                   
                    'number':fields.float("Mobile no"),
                    'num1' : fields.float('Num1'),
                    'num2' : fields.float('Num2'),
                    'total':fields.function(_total_num,type='float',string='Total'),
                    'student_id':fields.many2one('res.book','Book'),
                    'name1': fields.char('Name'),              
                    'sum' : fields.function(_sum_total, type='float', string='Sum',multi='asd'),
                    'sum1' : fields.function(_sum_total, type='float', string='Sum1',multi='asd'), 
                   # 'dob' : fields.date('Date of Birth',required=True),
                   # 'age' : fields.integer('Age'),
                }
    _defaults = {
                'name':'ilesh',
                
                }
    def many2one(self,cr,uid,id,context=None):
        #stage = self.pool.get('res.book')
        browes = self.browse(cr,uid,id)
        print 'name  res.class(1,)'
        
        print browes.student_id
    def print_quotation(self, cr, uid, ids, context=None):
        
#         stage = self.pool['report'].get_action(cr, uid, ids, 'student.qweb_report_demo', context=context)
#         print stage
        return {
                
                'type':'ir.actions.report.xml',
                'report_name': 'student.qweb_report_demo',
                'data': None 
                
                }
        
 
#     def main_val(self,cr,uid,ids,context=None):
#         stage = self.pool.get('res.book')
#         browes = self.browse(cr,uid,id)
#         print browes.name
#    
   
#     def birth_date(self,cr,uid,ids,dob):
#         values = {}
#         age = 0
#   
#         current_date = datetime.now()
#         print current_date         
#         dob = datetime.strptime(dob,"%Y-%m-%d")
#         print dob
#         if dob:    
#                   
#             if current_date < dob:
#                 warning = {
#                             'title': 'Invalid Birth Date!',
#                             'message' : 'Enter Currect Birth date.'
#                                 }
#                 return {'warning': warning} 
#             else:
#                 a = current_date.day - dob.day
#                 print a
#                 age = a / 8365 
#                 print age
#                       
#             values = {'age': age}
#             return {'value' : values}



   # def unlink(self, cr, uid, ids,context=None):
            #stage = self.unlink(cr, uid, [5])
          #  print stage
         #  value = self.browse(cr,uid,ids,values)
         #  print value.name
         #  if value.name == 'nikunj'ValueError: invalid literal for float(): 363 days, 0:00:00ValueError: invalid literal for float(): 363 days, 0:00:00:
          #     raise osv.except_osv(('This name can not modify'),('go to next filed modify'))
           #else:
    #        value = super(res_student, self).browse(cr,uid,ids)
    #        print value.name
     #       if value.name == 'nikunj':
                
#                 raise osv.except_osv(('this record can not delete'),('go to next filed modify'))
#                 
#             else:
#                return super(res_student, self).unlink(cr, uid,ids, context)
#     
#     def write(self,cr, uid, ids, values, context=None):
         #stage = self.write(cr,uid,[19],{'name':'nikunj',})
       # print stage
    #  res = super(res_student, self).write(cr, uid, ids, {'name':'jay'}, context = context)
     # if 'child_field' in values:
      #    for child_item in self.browse(cr, uid, ids, context = context):
       #         self.pool.get('res.student').write(cr, uid, ids, {'name': values['child_field'],}, context = context)
      # values['number'] = 0
       #if(number == 0):
        #    raise osv.except_osv(('invalid mobile number'), ('Enter currect  number'))
       
#             value = self.browse(cr,uid,ids,values)
#             print value.name
#             if value.name == 'sagar':
#                 raise osv.except_osv(('This name can not modify'),('go to next filed modify'))
#                 return super(res_student, self).write(cr, uid,ids,{'name':'sagar'}, context=context)
#             else:
#                 return super(res_student, self).write(cr, uid,ids,values, context=context)
#            
#     def copy(self, cr, uid, id, defaults,context=None):             
#          #stage= self.copy(cr, uid,[17],{'name':'jay'})
#          stage = super(res_student, self).copy(cr, uid,id,{'name':'nikunj'}, context=context)
#          print stage
#          return stage
   # def read(self,cr, uid, ids, fields=None, context=None):
    #    value = super(res_student, self).read(cr,uid,ids,fields,context)
     #   print value[0]['name']
      #  if value[0]['name'] == 'ilesh':
     
       #     return super(res_student, self).write(cr, uid, ids, {'name':'jay'}, context=context)
       # else:
        #    stage = super(res_student, self).read(cr, uid,ids, fields, context=context)
         #   return stage
    
   # def create(self,cr,uid,ids,context=None):
   #   stage = self.create(cr,uid, {'name':'jaydip'},context=context)
    #  print stage
     # print uid
     # print ids
    
    #  return super(res_student, self).create(cr, uid, {'name':'nikunj'}, context=context)
#     def def_search(self,cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
#         stage = self.search(cr, uid, [ '|', ('name', '!=', 'jay'),'!', ('name', 'ilike', 'spam'),],)
#         print stage
#         print uid
#         return stage
class res_book(osv.osv):
    _name='res.book'
    _columns={
              'name' : fields.char("Book Name"),
              'price' : fields.integer("Price"),
              'author' : fields.char("Authore"),
              'student_ids' : fields.one2many('res.student','student_id',"Student"),
             # 'book_ids':fields.many2many('book.student_rel','student_id','book_id','Books'),
            }
    def one2many(self,cr,uid,id,context=None):
       # stage = self.pool.get('res.book')
        browes = self.browse(cr,uid,id)
        print 'name  res.student(16,)'
        print browes.student_ids
        
class school(osv.osv):
    _name='book.student_rel'
    _columns={
              'class' : fields.char('Class'),
              'student_id':fields.many2one('res.book','Book'),
              'book_id':fields.char('Book'),
              } 
class res_class(osv.osv):
    _name = 'res.class'
    _rec_name="class"
    _columns={
                'class': fields.char("Class"),
              }
    
class sale_order(osv.osv):
    _inherit = 'sale.order'
    _columns={
              
              'skype' : fields.char("Skype"),
              
                 }
    
class sale_order_line(osv.osv):
    _inherit='sale.order.line'
    _columns={
                'skype1' : fields.char("Skype"),
              }
    
    
    
    
class invoice(osv.osv):
    _inherit = 'account.invoice.line'
    _columns = {
                'skype':fields.char("skype"),
                }

