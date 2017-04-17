import math
class Vector(object):
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
   
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    def magnitude(self):
        total = 0
        for x in self.coordinates:
            total = total + x*x
        return total**(1/2)
    
    def normalization(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalized zero vector")
            
    def dot(self,v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def angle(self,v, in_degree=False):
        try:
            magnitude1 = self.magnitude()
            magnitude2 = v.magnitude()
            angle = math.acos(self.dot(v) / (magnitude1 * magnitude2))
            if in_degree:
                return angle* 180 / math.pi
            else:
                return angle
        except ZeroDivisionError:
            raise Exception("Cannot normalized zero vector")
   
    
    def parallel(self,v):
        return self.is_zero() or v.is_zero() or self.angle(v) == 0 or self.angle(v) == math.pi
        
    
    def orthogonal(self,v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance
    
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    
    def component_parallel_to(self,basis):
        try:
            u = basis.normalization()
            weight = self.dot(u)
            return u.times_scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
    
    def component_orthogonal_to(self,basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_orthogonal_COMPONENT_MSG)
            else:
                raise e
    
    
    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates

            return Vector([y_1 * z_2 - y_2 * z_1, -(x_1 * z_2 - x_2 * z_1), x_1 * y_2 - x2_2 * y1])
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif msg == 'too many values to unpack' or msg == 'need more than value to unpack':
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        return self.cross(v).magnitude()
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
