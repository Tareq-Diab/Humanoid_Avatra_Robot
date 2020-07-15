import math
class vector ():
    """
    Definition of a vector
A vector is an object that has both a magnitude and a direction. Geometrically, 
we can picture a vector as a directed line segment, whose length is the magnitude of 
the vector and with an arrow indicating the direction. 
The direction of the vector is from its tail to its head.
Two vectors are the same if they have the same magnitude and direction. This means that
if we take a vector and translate it to a new position (without rotating it), then the vector 
we obtain at the end of this process is the same vector we had in the beginning.

Two examples of vectors are those that represent force and velocity. Both force and velocity are
 in a particular direction. The magnitude of the vector would indicate the strength of the force 
 or the speed associated with the velocity.

We denote vectors using boldface as in a or b. Especially when writing by hand where one cannot easily
 write in boldface, people will sometimes denote vectors using arrows as in a⃗  or b⃗ , or they use other markings.
  We won't need to use arrows here. We denote the magnitude of the vector a by ∥a∥. When we want to refer to a number
   and stress that it is not a vector, we can call the number a scalar. We will denote scalars with italics, as in a or b.

You can explore the concept of the magnitude and direction of a vector using the below applet. Note that moving the vector 
around doesn't change the vector, as the position of the vector doesn't affect the magnitude or the direction. But if you stretch
 or turn the vector by moving just its head or its tail, the magnitude or direction will change. (This applet also shows the coordinates
  of the vector, which you can read about in another page.)
    """
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
                    
    
