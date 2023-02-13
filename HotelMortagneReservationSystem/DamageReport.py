class DamageReport:

    def _inti_(self, damage_id, damage_description, damage_date, damage_balance):
        self.damage_id = damage_id
        self.damage_description = damage_description
        self.damage_date = damage_date
        self.damage_balance = damage_balance

    #getter and setter for damage id
    def _set_damage_id(self, id):
        self.damage_id = id
    
    def _get_damage_id(self):
        return self.damage_id
    
    #getter and setter for damage description
    def _set_damage_description(self, desc):
        self.damage_description = desc
    
    def _get_damage_description(self):
        return self.damage_description
    
    #getter and setter for damage date
    def _set_damage_date(self, date):
        self.damage_date = date
    
    def _get_damage_date(self):
        return self.damage_date
    

    #getter and setter for damage balance
    def _set_damage_balance(self, bal):
        self.damage_balance = bal

    def _get_damage_balance(self):
        return self.damage_balance
        

