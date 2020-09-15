# Métodos de Projeto de Software
## Lista de nivelamento POO

### Questão 1

a. Uma vantagem da POO sobre a Programação Estruturada é que ela possui um melhor reaproveitamento de código, já que podem ser criadas instâncias, relacionar e herdar atributos dos objetos para outras aplicações.

b. É uma instância de uma classe, um conjunto de dados que possui atributos e métodos.

c. Propriedade estática é quando é determinado o tipo do objeto em tempo de compilação, sem ocorrer sobrescrita de método. Propriedade dinâmica é quando o método de uma classe é sobrescrito pelo método de outra classe com mesmo nome, isso acontece quando tem herança, e o seu tipo é determinado em tempo de execução.

Exemplo estático:

	Class print_1{
		public static void func (){
			print(“1”)
	}
	}

	Classe print_2 extends print_1{
		public static void func (){
			print(“2”)
	}
	public static void main(){
			print_1 obj = new print_2();
	obj.func();
	}
	}

	saída: “1”

Exemplo dinâmico:

	Class print_1{
		public void func (){
			print(“1”)
	}
	}

	Classe print_2 extends print_1{
		public void func (){
			print(“2”)
	}
	public void main(){
			print_1 obj = new print_2();
	obj.func();
	}
	}

	saída: “2”

d. Encapsulamento é a maneira de ocultar determinados atributos e métodos de uma classe das demais classes. É importante encapsular para que o sistema esteja pronto para modificações.

e. O estado de um objeto são os valores dos atributos dele. O comportamento é relacionado aos seus métodos.

f.  [Código](https://github.com/caiovictors/Metodos-de-Projetos-de-Software/blob/master/Lista%201/codigo_class.py)

g. É a localização do objeto na memória.

h. A referência irá receber a nova referência do novo objeto

i. Classe é uma estrutura que agrupa objetos com características similares, como métodos e atributos. Ela serve para definir o comportamento e estados dos objetos. Exemplo de classe em python: [código](https://github.com/caiovictors/Metodos-de-Projetos-de-Software/blob/master/Lista%201/codigo_class.py)

j. Uma variável de classe possui um valor comum a todos os objetos que pertencerem à classe, e uma variável de instância possui um valor específico para cada objeto. O nome é sobrecarga (overload). Para distinguir um método do outro, eles precisam possuir argumentos diferentes, por exemplo:

public class calculadora{
public int calcula( int a, int b){
    return a+b;
  }
  public double calcula( double a, double b){
     return a+b;
  }
   public String calcula( String a, String b){
     return a+b;
}
}

k. this = referência à própria classe
this() = chama o construtor da própria classe.
super = referência à classe mãe.
super() = chama o construtor da classe mãe.

l. oo

m. Um Error não pode ser tratado pela aplicação, enquanto os exceptions podem ser capturadas e tratadas via try e catch.

n. try-catch: no try fica a parte do código onde pode ser lançada uma exceção e no catch é a ação que ocorrerá caso a exceção seja capturada.
throw e throws: throws serve para tratar uma exceção em um outro bloco chamado por ele, enquanto o throw lança uma exceção padrão invés de uma específica.
finally: é usado quando é necessário que uma ação seja tomada mesmo após a captura de uma exceção.

