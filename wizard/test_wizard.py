from openerp.osv import osv,fields


class test_wizard(osv.osv_memory):
    _name = "student.wizard"
    
    _columns = {
                'old' : fields.many2one('res.student','Old', required=True),
                'new' : fields.char('New', required=True),
            
                
                } 
    def add_student(self, cr, uid, id, context=None):
        print "ids------------",id
        print "---------------------------add_student---------------",self.browse(cr,uid,id)[0]
         
        for student in self.browse(cr,uid,id,context=context):
            print context
            print student.old
            print student.new
            self.pool.get('res.student').write(cr,uid,[student.old.id],{'name':student.new})
        return True
    def default_get(self, cr, uid, fields, context=None):  
        
        ret = super(test_wizard,self).default_get(cr, uid, fields, context=context)
        old = context.get('active_id',False)
        if old:
            ret['old'] = old
        return ret