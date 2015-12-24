from openerp.osv import osv,fields


class test_wizard(osv.osv_memory):
    _name = "custom.report"
    
    _columns = {
                'from_date' : fields.date('From Date', required=True),
                '' : fields.date('To Date', required=True),
            
                
                } 
    def report_print(self,cr,uid,id,context=None):
        stage = self.browse(cr,uid,id)
        list = {}
        list = {'to':stage.old,'from':stage.new}
        print list
        
        return self.pool['report'].get_action(cr, uid, id, 'student.qweb_report_demo', data=list)
        