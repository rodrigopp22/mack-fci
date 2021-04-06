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
public class Estagiario extends Funcionario {
    private double vale_coxinha;
        public Estagiario(int id, String nome, double salario, double vale_coxinha){
        super(id, nome, salario);
        this.vale_coxinha = vale_coxinha;
    }
    public double getSalario(){
        return(super.getSalario() + this.vale_coxinha);
    }
}
