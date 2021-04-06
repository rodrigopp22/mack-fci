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
public class Secretaria extends Funcionario{
    private double previdencia;
    public Secretaria(int id, String nome, double salario){
        super(id, nome, salario);
        this.previdencia = 0.05;
    }
    public double getSalario(){
        return(super.getSalario()*(1 - this.previdencia));
    }
}
