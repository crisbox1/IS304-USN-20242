import java.util.Random;
import java.util.Scanner;

public class Sudoku {
    private int[][] matriz;
    private Random random;

    // Constructor para inicializar el tablero vacío
    public Sudoku() {
        matriz = new int[9][9];
        random = new Random();
    }

    // Método para mostrar el tablero de Sudoku
    public void mostrarTablero() {
        System.out.println("Tablero de Sudoku:");
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i != 0) {
                System.out.println("---------------------");
            }
            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0 && j != 0) {
                    System.out.print("| ");
                }
                System.out.print(matriz[i][j] == 0 ? ". " : matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Método para ingresar un número en una posición específica
    public boolean ingresarNumero(int fila, int columna, int numero) {
        if (!esPosicionValida(fila, columna) || !esNumeroValido(numero)) {
            System.out.println("Número o posición inválida.");
            return false;
        }

        if (matriz[fila][columna] != 0) {
            System.out.println("La celda ya está ocupada. ¿Desea modificar el número? (sí/no): ");
            Scanner scanner = new Scanner(System.in);
            String respuesta = scanner.next();
            if (!respuesta.equalsIgnoreCase("sí")) {
                return false;
            }
        }

        if (esValido(fila, columna, numero)) {
            matriz[fila][columna] = numero;
            if (esSubcuadroLleno(fila, columna)) {
                System.out.println("¡Uno de los subcuadros de 3x3 está completamente lleno!");
            }
            return true;
        } else {
            System.out.println("Número no válido. Verifique las reglas del Sudoku.");
            return false;
        }
    }

    // Validar si la posición es válida
    private boolean esPosicionValida(int fila, int columna) {
        return fila >= 0 && fila < 9 && columna >= 0 && columna < 9;
    }

    // Validar si el número es válido
    private boolean esNumeroValido(int numero) {
        return numero >= 1 && numero <= 9;
    }

    // Método para validar que el número no se repita en la fila, columna o subcuadro 3x3
    private boolean esValido(int fila, int columna, int numero) {
        return !esNumeroEnFila(fila, numero) &&
               !esNumeroEnColumna(columna, numero) &&
               !esNumeroEnSubcuadro(fila, columna, numero);
    }

    private boolean esNumeroEnFila(int fila, int numero) {
        for (int j = 0; j < 9; j++) {
            if (matriz[fila][j] == numero) {
                return true;
            }
        }
        return false;
    }

    private boolean esNumeroEnColumna(int columna, int numero) {
        for (int i = 0; i < 9; i++) {
            if (matriz[i][columna] == numero) {
                return true;
            }
        }
        return false;
    }

    private boolean esNumeroEnSubcuadro(int fila, int columna, int numero) {
        int inicioFila = (fila / 3) * 3;
        int inicioColumna = (columna / 3) * 3;
        for (int i = inicioFila; i < inicioFila + 3; i++) {
            for (int j = inicioColumna; j < inicioColumna + 3; j++) {
                if (matriz[i][j] == numero) {
                    return true;
                }
            }
        }
        return false;
    }

    // Método para verificar si un subcuadro 3x3 está completamente lleno
    private boolean esSubcuadroLleno(int fila, int columna) {
        int inicioFila = (fila / 3) * 3;
        int inicioColumna = (columna / 3) * 3;
        for (int i = inicioFila; i < inicioFila + 3; i++) {
            for (int j = inicioColumna; j < inicioColumna + 3; j++) {
                if (matriz[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    // Método para llenar el tablero con una cantidad aleatoria de números válidos
    public void llenarTableroConNumerosAleatorios(int cantidad) {
        int numerosColocados = 0;

        while (numerosColocados < cantidad) {
            int fila = random.nextInt(9);
            int columna = random.nextInt(9);
            int numero = random.nextInt(9) + 1;

            if (matriz[fila][columna] == 0 && esValido(fila, columna, numero)) {
                matriz[fila][columna] = numero;
                numerosColocados++;
            }
        }
    }

    // Método principal para jugar al Sudoku
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Sudoku sudoku = new Sudoku();

        System.out.println("Elija una opción:");
        System.out.println("1. Iniciar con un tablero vacío");
        System.out.println("2. Iniciar con números aleatorios (entre 9 y 21)");

        int opcion = scanner.nextInt();

        if (opcion == 2) {
            int cantidad = sudoku.random.nextInt(13) + 9; // Generar una cantidad aleatoria entre 9 y 21
            sudoku.llenarTableroConNumerosAleatorios(cantidad);
        }

        boolean jugar = true;

        while (jugar) {
            sudoku.mostrarTablero();

            System.out.print("Ingrese la fila (0-8): ");
            int fila = scanner.nextInt();

            System.out.print("Ingrese la columna (0-8): ");
            int columna = scanner.nextInt();

            System.out.print("Ingrese el número (1-9): ");
            int numero = scanner.nextInt();

            boolean ingresoExitoso = sudoku.ingresarNumero(fila, columna, numero);
            if (!ingresoExitoso) {
                System.out.println("Intento fallido. Intente de nuevo.");
            }

            System.out.print("¿Desea continuar? (sí/no): ");
            String respuesta = scanner.next();
            if (respuesta.equalsIgnoreCase("no")) {
                jugar = false;
            }
        }

        scanner.close();
        System.out.println("¡Gracias por jugar al Sudoku!");
    }
}
