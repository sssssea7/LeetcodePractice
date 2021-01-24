class Solution(object):
    def getImportance(self, employees, id):
        imp={}
        emp={}
        for e in employees:
            imp[e.id]=e.importance
            emp[e.id]=e.subordinates
            
        self.value = imp[id]
        
        def dfs(subs):   # [2,3]
            if not subs:
                return
            for sub in subs:      # id
                self.value += imp[sub]
                dfs(emp[sub])
        dfs(emp[id])
        return self.value