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
public class Funcionario {
    private int ID;
    private String nome;
    private double salario;
    public Funcionario(int id, String nome, double salario){
        this.ID = id;
        this.nome = nome;
        this.salario = salario;
    }
    public int getId(){
      return(this.ID);
    }
    public String getNome(){
      return(this.nome);
    }
    public double getSalario(){
        return(this.salario);
    }
    @Override
    public String toString(){
      return "Funcionario: " + this.getId() + "; Nome: " + this.getNome() + "; Salario: R$" + this.getSalario(); 
    }
}
