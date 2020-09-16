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
	}

k. this = referência à própria classe </br>
this() = chama o construtor da própria classe. </br>
super = referência à classe mãe. </br>
super() = chama o construtor da classe mãe. </br>

l. Erros de execução na linguagem C: Runtime error, segmentation fault, stack overflow.

m. Um Error não pode ser tratado pela aplicação, enquanto os exceptions podem ser capturadas e tratadas via try e catch.

n. try-catch: no try fica a parte do código onde pode ser lançada uma exceção e no catch é a ação que ocorrerá caso a exceção seja capturada.
throw e throws: throws serve para tratar uma exceção em um outro bloco chamado por ele, enquanto o throw lança uma exceção padrão invés de uma específica.
finally: é usado quando é necessário que uma ação seja tomada mesmo após a captura de uma exceção.

### Questão 2
A classe abaixo foi desenvolvida na disciplina Linguagem de programação I em C++, cujo nome é Data, ela define dia, mês e ano e o construtor inicializa um objeto (no cpp para 1/1/1970): 

	#ifndef DATA_H_
	#define DATA_H_

	class Data {
		private:      
			int dia;  //atributo
			int mes;  //atributo
			int ano;  //atributo
		public:
			Data();    //construtor padrao
			Data(int, int, int);  //construtor personalizado
			int getDia();  //metodo para pegar o dia
			int getMes();  //metodo para pegar o mes
			int getAno();  //metodo para pegar o ano
			void setDia(int);  //metodo para setar o dia
			void setMes(int);  //metodo para setar o mes
			void setAno(int);  //metodo para setar o ano
			bool verificaData();  //metodo para verificar a data
			void avancarDia();  //metodo para avancar um dia
	};

	#endif /* DATA_H_ */

A classe abaixo “model” pertence a um projeto em grupo de computação gráfica, cada objeto posto em cena é um modelo, com seus atributos. O código não irá compilar sem as bibliotecas de computação gráfica instaladas. Código em C++:
	
	#ifndef MODEL_HPP
	#define MODEL_HPP
	#include "include.hpp"

	class Model{
		private:
		    unsigned int vaoId; //ID do modelo
		    unsigned int vertexCount; //Número de vértices
		    unsigned int textureId; //ID da textura que o modelo vai receber

		public:
		    glm::vec3 rotation; //Vetor do tipo glm que compõe a rotação do corpo
		    glm::vec3 scale; //Vetor do tipo glm que compõe a escala/dimensão do corpo
		    glm::vec3 position; //Vetor do tipo glm que compõe a posição do modelo na cena

		    Model(); //Construtor que irá setar todos esses atributos para 0, incluindo os vetores, e os valores são preenchidos fora da classe
	};
	#endif

Ainda no projeto de computação gráfica, a classe iluminação define a luz direcional (o sol por exemplo). Código em C++.

	#ifndef LIGHTING_HPP
	#define LIGHTING_HPP
	#include "include.hpp"
	
	class lighting{
		private:
		    glm::vec3 lightPosition; // Vetor do tipo glm que guarda as coordenadas da luz
		public:
	};

	#endif

