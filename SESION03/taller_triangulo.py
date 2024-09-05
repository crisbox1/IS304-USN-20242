//Cristian felipe sanchez guzman
public class Main {
    public static void main(String[] args) {
        Triangulo c = new Triangulo(5,9);
        Triangulo_Rectangulo r = new Triangulo_Rectangulo(9,8);
        
    }
    }


abstract class FiguraGeom {
    private String nombre;

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    abstract public double area();
    abstract public double perim();
}

class Triangulo extends FiguraGeom {
    private double base;
    private double altura;

    public Triangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
        setNombre("Triangulo");
    }

    public double area() {
        return 0.5 * base * altura;
    }

    
    public double perim() {
        return 3 * base;
    }
}

class Triangulo_Rectangulo extends FiguraGeom {
    private double base;
    private double altura;

    public Triangulo_Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
        setNombre("Triangulo_Rectangulo");
    }

    public double area() {
        return 0.5 * base * altura;
    }

  
    public double perim() {
        double hypotenuse = Math.sqrt(base * base + altura * altura);
        return base + altura + hypotenuse;
    }
}
