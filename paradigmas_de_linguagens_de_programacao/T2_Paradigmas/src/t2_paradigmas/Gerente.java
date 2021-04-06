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
public class Gerente extends Funcionario{
    private double previdencia, adicional;
    public Gerente(int id, String nome, double salario, double adicional){
        super(id, nome, salario);
        this.previdencia = 0.07;
        this.adicional = adicional;
    }
    public void alteraAdicional(double novo_percentual){
            this.adicional = adicional*(1+novo_percentual);
    }
    public double getSalario(){
        return (super.getSalario()*((1 - this.previdencia) + this.adicional));
    }
}
