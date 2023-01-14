package tw4;

//superclass
class Circle{
	double radius;
	String color;
	
	Circle(){
		radius = 1.0;
		color="Red";
	}
	Circle(double radius){
		this.radius=radius;
		color="Red";
	}
	Circle(double radius, String color){
		this.radius=radius;
		this.color=color;
	}
	double getRadius() {
		return radius;
	}
	void setRadius(double radius) {
		this.radius=radius;
	}
	String getColor() {
		return color;
	}
	void setColor(String color) {
		this.color=color;
	}
	double getArea() {
		return (Math.PI*radius*radius);
	}
}
//subclass
class Cylinder extends Circle{
	double height;
	
	Cylinder(){
		super();
		height=1.0;
	}
	Cylinder(double height){
		super();
		this.height=height;
	}
	Cylinder(double height, double radius){
		super(radius);
		this.height=height;
	}
	Cylinder(double height, double radius, String color){
		super(radius,color);
		this.height=height;
	}
	double getHeight() {
		return height;
	}
	void setHeight(double height) {
		this.height=height;
	}
	double getVolume() {
		return (Math.PI*radius*radius*height);
	}
}

public class Tw4 {

	public static void main(String[] args) {
		
		Circle c=new Circle(3.0,"Violet");
		System.out.println("Radius of circle = "+c.getRadius()+"\nColor of Circle = "+c.getColor());
		c.setColor("Blue");
		System.out.println("Changed Color of the cirlce : "+c.getColor()+(String.format("\nThe Area of the circle : %.2f",c.getArea())));
		
		Cylinder c1=new Cylinder(3.0,4.0,"Green");
		System.out.println("Radius of the Cylinder : "+c1.getRadius()+"\nHeight of the Cylinder : "+c1.getHeight()+"\nColor of the Cylinder : "+c1.getColor()+String.format("\nVolume of the Cylinder : %.2f",c1.getVolume()));	
	}
}
