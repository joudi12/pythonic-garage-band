from abc import abstractmethod, ABC


class Band(ABC):
    all_bands =[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.all_bands.append(self)
    def play_solos(self):
        solo =[]
        if len(self.members) !=0:
            for i in self.members:
                solo.append(i.play_solo())
            return solo  
        else: 
            return 'There are no member' 
           
         
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        
        return f'{self.name}'  
    @classmethod
    def to_list(cls):
        return cls.all_bands 

class Musician(ABC): 



    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return  f'My name is {self.name} and I play {self.get_instrument()}'  
       

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'

    @abstractmethod    
    def get_instrument(self) :
        pass    
    @abstractmethod    
    def play_solo(self) :
        pass       


class Guitarist(Musician):
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'   


class Bassist(Musician):
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'




if __name__ == "__main__" :
    tbep = Band("The Black Eyed Peas", ['joudi','ff'])
    # print(tbep.name)
    guitarist = Guitarist("guitarist")
    print(guitarist)
    # print(repr(guitarist))
   
   