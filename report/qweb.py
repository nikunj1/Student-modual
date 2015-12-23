from openerp.report import report_sxw
from openerp.osv import osv

class qweb_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(qweb_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_index':self.get_index
                                })
     
    def get_index(self,product):
        print "\n\nproduct-----------------------"
        serial_number_ids = self.pool.get('sale.order.line').search(self.cr, self.uid, [('product_id','=',product.id)])
        return self.pool.get('sale.order.line').browse(self.cr, self.uid, serial_number_ids)


        
class report_test(osv.AbstractModel):
    _name = 'report.student.qweb_report_demo'
    _inherit = 'report.abstract_report'
    _template = 'student.qweb_report_demo'
    _wrapped_report_class = qweb_report