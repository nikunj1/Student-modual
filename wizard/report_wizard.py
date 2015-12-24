from openerp.osv import osv,fields


class test_wizard(osv.osv_memory):
    _name = "custom.report"
    
    _columns = {
                'from_date' : fields.date('From Date', required=True),
                'to_date' : fields.date('To Date', required=True),
            
                
                } 
    def report_print(self,cr,uid,id,context=None):
        stage = self.browse(cr,uid,id)
        list = {}
        list = {'to':stage.old,'from':stage.new}
        print list
        
        return {
                
                'type':'ir.actions.report.xml',
                'report_name': 'student.qweb_report_demo',
                'data': list 
                
                }
    