import math
class vector ():
    def __init__ (self,p1,p2):
        self.x1=p1[0]
        self.x2=p2[0]
        self.y1=p1[1]
        self.y2=p2[1]
        self.z1=p1[2]
        self.z2=p2[2]
        self.x_of_vector=self.x2-self.x1
        self.y_of_vector=self.y2-self.y1
        self.z_of_vector=self.z2-self.z1
    def update(self,p1,p2):
        self.x1=p1[0]
        self.x2=p2[0]
        self.y1=p1[1]
        self.y2=p2[1]
        self.z1=p1[2]
        self.z2=p2[2]
        self.x_of_vector=self.x2-self.x1
        self.y_of_vector=self.y2-self.y1
        self.z_of_vector=self.z2-self.z1




class angle():
    """
    https://www.intmath.com/vectors/7-vectors-in-3d-space.php
    θ=arccos(P⋅Q/∣P∣∣Q∣)
    """
    def get_angle(self,vector_1,vector_2):
        """
        usage example :
        vector_1=vector([0,0,0],[4,0,7])
        vector_2=vector([0,0,0],[-2,1,3])

        knee=angle()
        print(knee.get_angle(vector_1,vector_2))
        OUTPUT: 64.47240178232686
        """
        dot_product=[vector_1.x_of_vector*vector_2.x_of_vector+
                    vector_1.y_of_vector*vector_2.y_of_vector+
                    vector_1.z_of_vector*vector_2.z_of_vector]
        
        denominator=[math.sqrt(
                            math.pow(vector_1.x_of_vector,2)+
                            math.pow(vector_1.y_of_vector,2)+
                            math.pow(vector_1.z_of_vector,2))
                    *math.sqrt(
                            math.pow(vector_2.x_of_vector,2)+
                            math.pow(vector_2.y_of_vector,2)+
                            math.pow(vector_2.z_of_vector,2))
                            ]
        
        return math.acos(dot_product[0]/denominator[0])*57.2957795 
                    
    
