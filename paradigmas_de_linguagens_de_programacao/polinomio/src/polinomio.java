/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author digop
 */
public class polinomio {
    private int grau;
    private double vet[];
    public polinomio(int grau) {
        this.grau = grau;
        double vet[] = new double[this.grau + 1];
    }

    public void setTermo(double valor, int expoente) {
        this.vet[expoente] = valor;
    }

    public double getValor(int x) {
        double resultado=0; 
        int aux = 0;
        for (int i = 0; i < this.grau; i++) {
            resultado = this.vet[i] * Math.pow(x, i);
        }
        return resultado;
    }
}


