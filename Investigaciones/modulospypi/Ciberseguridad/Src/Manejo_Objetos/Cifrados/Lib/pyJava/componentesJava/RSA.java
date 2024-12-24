package Src.pyJava.componentesJava;

import java.math.BigInteger;
import java.security.KeyPair;
import java.security.PrivateKey;
import java.security.PublicKey;

public class RSA {

	public static void main(String[] args) {
		
		// TODO Cifrado Asincrono
		
		/*
		 * Es un tipo de cifrado en el que se generan una :
		 * 		clave Publica : es una clave que nos ayuda a cifrar texto,
		 * 		esta tiene que ser enviada a la persona con la que quieres
		 * 		escribirte por internet
		 * 		clave Privada : es una clave que nos ayuda a cifrar y descifrar texto,
		 * 		está no tiene que ser enviada, ni publicada, en internet, ya que, esta
		 * 		es un clave secreta, que no debe de saber nadie mas que el usuario
		 * 
		 * Este tipo de cifrado se utiliza cuando queremos proteger datos que esten
		 * en movimiento, como por ejemplo en un chat o una VPN, para entender esto
		 * diremos que este cifrado se utiliza cuando queremos enviar datos a algun
		 * lugar en la red.
		 * 
		 * */
		
		String texto = args[0];
		boolean modo = Boolean.parseBoolean(args[1]); 
		
		try {
			
			// 1º Generamos un clave publica y privada
			
			KeyPair keypair = GeneradorClavesRSA.generadorRSAclavePar();
			PrivateKey clave_Privada = keypair.getPrivate();
			PublicKey clave_Publica = keypair.getPublic();
			
			byte[] clave_publica = clave_Publica.getEncoded();
			byte[] clave_privada = clave_Privada.getEncoded();
			
			// clave_publica = keypair.getPublic().getEncoded();
			// clave_privada = keypair.getPrivate().getEncoded();
			
			// --------------- Codificamos a hexadecimal ----------------------
			
			BigInteger codificacion;
			
			codificacion = new BigInteger(1, clave_publica);
			
			System.out.println(codificacion.toString(16)); // Clave Publica
			
			codificacion = new BigInteger(1, clave_privada);
			
			System.out.println(codificacion.toString(16)); // Clave Privada
			
			// System.out.println(codificacion.toString(16).length());
			// System.out.println(new BigInteger(1, clave_Privada.getEncoded()).toString(16));
			
			// 2º Encriptamos el texto
			
			byte[] textoCifrado = OperacionesRSA.encriptacionRSA(texto, clave_Publica);
			
			// ---------------- Codificamos a hexadecimal ------------------------
			
			BigInteger codificacion2 = new BigInteger(1, textoCifrado);
			
			System.out.println(codificacion2.toString(16)); // Texto encriptado codificado a hexadecimal
			
			// 3º Desencriptamos el texto
			
			String textoDescifrado = OperacionesRSA.desencriptacionRSA(textoCifrado, clave_Privada);
			
			System.out.println(textoDescifrado); // Texto desencriptado
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		// https://www.geeksforgeeks.org/asymmetric-encryption-cryptography-in-java/
		// https://ciberseguridad.com/servicios/algoritmos-cifrado/
		
	}

}
