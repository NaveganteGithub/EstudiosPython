package Src.pyJava.componentesJava;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;

public class GeneradorClavesRSA {

	private static String RSA = "RSA";
	
	GeneradorClavesRSA() {}
	
	public static KeyPair generadorRSAclavePar() throws Exception {
		
		/* 
		 * Esta clase sirve para pedir un generador 
		 * de numero aleatorio fuerte criptograficamente o RNG
		 * 
		 * Un Numero Aleatorio fuerte criptograficamente
		 * es un numero generado aleatoriamente y que 
		 * cumple minimo las pruebas especificadas en
		 * los estandares de Generador de Numero Aleatorio :
		 * 			FIPS 140-2
		 * 			Security Requirements for Cryptographic Modules
		 * que son estandares para comprobar si el Generador de Numero 
		 * Aleatorio a generado un numero que sea fuerte Criptograficamente
		 * 
		 * Para mi sintetización personal digo que SecureRandom es como el
		 * Random pero para generar numeros aleatorios decimales para la
		 * Criptografia, pues si miramos la clase SecureRandom podemos
		 * comprobar que SecureRandom es una clase "hijo" de la clase
		 * java.util.Random, o sea de la clase Random.
		 * 
		 * */
		SecureRandom secureRandom = new SecureRandom();
		
		// Esta clase sirve para crear un generador de una clave publica y una clave privada
		KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance(RSA);
		
		/* 
		 * Este metodo inicializa la clase KeyPairGenerator, indicando que la clave va a tener 
		 * una longitud de 2048 bytes y se le va a pasar el numero aleatorio generado por
		 * el SecureRandom.
		 */ 
		keyPairGenerator.initialize(2048, secureRandom);
		
		return keyPairGenerator.generateKeyPair();
	}
	
}
