vec = [1,2,3];
vec1 = ["asd","adada"];
vec3 = [2,3,4];

#MultiEscalar:
multiplicacionEscalar([1,2,3],5,true OR false);
multiplicacionEscalar([1.2,2.3,3.3],4);
multiplicacionEscalar([1.2,2.3,3.3],4,(NOT false));	
multiplicacionEscalar(vec,1);
vec2 = multiplicacionEscalar(vec,1);
vec2[1] = 2;

#Capitalizar:
a = capitalizar("asd");
a += "d";
b = "asd";
a = capitalizar(b);
a = capitalizar(vec1[0]);
g =  "asd" + capitalizar("asd");

#Colineales:

t = colineales(vec,vec3);
t = colineales([1],[1]);
vec4 = [1.2];
t = colineales(vec4,vec2);
a = t OR false;
a = NOT(t OR false) == true;
a = colineales(multiplicacionEscalar([1,2],2),multiplicacionEscalar([2,2],2));

#Print:

print("asd");
print(vec3);
print(vec4);
print(a);
print(false);
print(false OR true);

#Length:

length(capitalizar(b));
length("asd"+"asd");
length([1,2]);
length(vec1);
a = length([1,2]);
vec[0] = a;
