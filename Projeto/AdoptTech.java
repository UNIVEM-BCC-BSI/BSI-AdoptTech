package org.example;
import java.util.ArrayList;
import java.util.Scanner;

public class AdoptTech {
    public static void main(String[] args) {
        ArrayList<Crianca> criancas_disponiveis = new ArrayList<Crianca>();
        String linhas = "=".repeat(50);
        int opcao;

        System.out.println("Bem-vindo ao AdoptTech!");

        do {
            System.out.println(linhas);
            System.out.println("Escolha uma opção:");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Consultar");
            System.out.println("3 - Sobre");
            System.out.println("4 - Sair");
            System.out.println(linhas);

            opcao = Integer.parseInt(new Scanner(System.in).nextLine());

            switch (opcao) {
                case 1:
                    System.out.println(linhas);
                    System.out.print("Digite o nome da criança: ");
                    String nome = new Scanner(System.in).nextLine();
                    System.out.print("Digite a idade da criança: ");
                    int idade = Integer.parseInt(new Scanner(System.in).nextLine());
                    System.out.print("Digite o gênero da criança (masculino, feminino ou não-binário): ");
                    String genero = new Scanner(System.in).nextLine();
                    criancas_disponiveis.add(new Crianca(nome, idade, genero));
                    System.out.println(linhas);
                    System.out.println(nome + " foi cadastrada com sucesso para adoção!");
                    break;
                case 2:
                    if (criancas_disponiveis.size() == 0) {
                        System.out.println(linhas);
                        System.out.println("Não há crianças disponíveis para adoção.");
                    } else {
                        System.out.println(linhas);
                        System.out.println("As seguintes crianças estão disponíveis para adoção:");
                        for (Crianca crianca : criancas_disponiveis) {
                            System.out.println("- " + crianca.nome + ", " + crianca.idade + " anos, " + crianca.genero);
                        }
                    }
                    break;
                case 3:
                    System.out.println(linhas);
                    System.out.println("O AdoptTech tem como objetivo ajudar a encontrar lares para crianças.");
                    break;
                case 4:
                    System.out.println(linhas);
                    System.out.println("Obrigado por usar o AdoptTech. Até a próxima!");
                    System.out.println(linhas);
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }

        } while (opcao != 4);
    }
}

class Crianca {
    String nome;
    int idade;
    String genero;

    public Crianca(String nome, int idade, String genero) {
        this.nome = nome;
        this.idade = idade;
        this.genero = genero;
    }
}
