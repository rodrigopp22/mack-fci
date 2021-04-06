package t2_paradigmas;
    import java.util.ArrayList;
public class Empresa {
    private ArrayList<Funcionario> empresa;

  public Empresa(){
    empresa = new ArrayList<Funcionario>();
  }
  public void adicionarFuncionario(int n, int id, String nome, double salario, double extra){
    if(n == 1){
      Estagiario e1 = new Estagiario(id, nome, salario, extra); 
      empresa.add(e1);
    }
    else if(n == 2){
      Secretaria s1 = new Secretaria(id, nome, salario);
      empresa.add(s1);
    }
    else if(n == 3){
      Gerente g1 = new Gerente(id, nome, salario, extra);
      empresa.add(g1);
    }
    else if(n == 4){
      Presidente p1 = new Presidente(id, nome, salario);
      empresa.add(p1);
    }
  }

  public double calculaPagto(int id){
    int pos=0;
    for(int i = 0; i < empresa.size(); i++){
      if(empresa.get(i).getId() == id){
        pos = i;
      }
    }
    double salario = empresa.get(pos).getSalario();
    return salario;
  }

  public void aumentaAdicional(double aumento){
    for(int i = 0; i < empresa.size(); i++){
      if(empresa.get(i) instanceof Presidente){
         ((Presidente) empresa.get(i)).alteraAdicional(aumento);
         
      }else if(empresa.get(i) instanceof Gerente){
         ((Gerente) empresa.get(i)).alteraAdicional(aumento);
          
      }
    }
  }
  public void geraRelatorio(){
    for(Funcionario f : empresa){
      System.out.println(f);
    }
  } 
}
