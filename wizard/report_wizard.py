from openerp.osv import osv,fields
import time

class test_wizard(osv.osv_memory):
    _name = "custom.report"
    
    _columns = {
                'from_date' : fields.datetime('From Date', required=True),
                'to_date' : fields.datetime('To Date', required=True),
            
                
                } 
    def report_print(self,cr,uid,id,context=None):
        #sheet_pool = self.pool.get('res.student')

        
        stage = self.browse(cr,uid,id)
        list = {}
        list = {'from_date':stage.from_date,'to_date':stage.to_date}
        
        
        
        return self.pool['report'].get_action(cr, uid, id, 'student.qweb_report_demo', data=list)
        