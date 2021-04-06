/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package t2_paradigmas;

/**
 *
 * @author digop
 */
public class Presidente extends Funcionario{
    private double previdencia, adicional_whisky, adicional_helicoptero, adicional_adicional;
    public Presidente(int id, String nome, double salario){
        super(id, nome, salario);
        this.previdencia = 0.15;
        this.adicional_whisky = 0.9;
        this.adicional_helicoptero = 0.7;
        this.adicional_adicional = 3.8;
    }
    void alteraAdicional(double novo_percentual){
        this.adicional_whisky = 0.9*(1+novo_percentual);
        this.adicional_helicoptero = 0.7*(1 + novo_percentual);
        this.adicional_adicional = 3.8*(1+novo_percentual);
    }
    public double getSalario(){
        return (super.getSalario()*((1-this.previdencia)+this.adicional_whisky + this.adicional_helicoptero + this.adicional_adicional));
    }
}
    