/*
UNIVERSIDADE PRESBITERIANA MACKENZIE
FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO - TRABALHO 2

NOME: FELIPE JOSÉ RICO RAGAZZI - TIA: 41807413
NOME: RODRIGO PIGATTO PASQUALE - TIA: 41816080
*/

package t2_paradigmas;

    import java.util.Scanner;

public class T2_Paradigmas {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    Empresa XYZ = new Empresa();
    boolean opc = true;
    int id, cat;
    String nome;
    double salario, adicional, aumento;
    while(opc){
      System.out.println("\n\nDigite:\n0 - sair;"
          + "\n1 - adicionar um funcionario;"
          + "\n2 - calcular pagamento do funcionario;"
          + "\n3 - aumentar o adicional de todos os funcionarios;"
          + "\n4 - relatiorio dos funcionarios da empresa;");
    int opcao = scanner.nextInt();
    switch(opcao){
      case 0:
        opc = false;
        break;
      case 1:
        System.out.println("Digite a categoria do funcionario: 1 - estagiario, 2 - secretaria, 3 - gerente, 4 - presidente;");
        cat = scanner.nextInt();
        System.out.println("Digite o ID do funcionario: ");
        id = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Digite o nome do funcionario: ");
        nome = scanner.nextLine();
        System.out.println("Digite o salario do funcionario:");
        salario = scanner.nextDouble();
        System.out.println("Caso o funcionario tenha adicional, digite-o, caso contrario digite -1: ");
        adicional = scanner.nextDouble();
        XYZ.adicionarFuncionario(cat, id, nome, salario, adicional);
        System.out.println("Funcionario adicionado com sucesso!");
        break;
      case 2:
        System.out.println("Digite o ID do funcionario que deseja calcular o pagamento: ");
        id = scanner.nextInt();
        System.out.println("O pagamento do funcionario eh: " + XYZ.calculaPagto(id));
        break;
      case 3:
        System.out.println("Digite o valor do percentual de aumento para os funcionarios: ");
        aumento = scanner.nextDouble();
        XYZ.aumentaAdicional(aumento);
        break;
      case 4:
        XYZ.geraRelatorio();
        break;
      default:
        System.out.println("\n\n\n\n\nErro! Comando inválido!");   
    }  
    }
    }
    
}
