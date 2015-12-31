from openerp.report import report_sxw
from openerp.osv import osv

product = 0
class qweb_report(report_sxw.rml_parse):
   
    
    def __init__(self, cr, uid, name, context):
        super(qweb_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_index':self.get_index,
            'get_data' :self.get_data
                                })
    def get_data(self,data):
        report_obj = self.pool.get('custom.report')
      
        catch = report_obj.browse(self.cr, self.uid, self.ids)
        print catch.from_date
        print catch.to_date
        sale_order_ids = self.pool.get('sale.order').search(self.cr,self.uid,
            [('create_date', '<=', catch.to_date),('create_date', '>=', catch.from_date)])
    
        print sale_order_ids
        sheet_browse = self.pool.get('sale.order').browse(self.cr, self.uid, sale_order_ids)
        print 'sheet'
        print sheet_browse
        return  sheet_browse
        
    def get_index(self,index):
        print "\n\nproduct-----------------------"
        global product
        product += 1
    
        return product


        
class report_test(osv.AbstractModel):
    _name = 'report.student.qweb_report_demo'
    _inherit = 'report.abstract_report'
    _template = 'student.qweb_report_demo'
    _wrapped_report_class = qweb_report