package Src.pyJava.componentesJava;

import java.security.PrivateKey;
import java.security.PublicKey;
import javax.crypto.Cipher;

public class OperacionesRSA {
	
	private static String RSA = "RSA"; 
	
	public OperacionesRSA() {}
	
	public static byte[] encriptacionRSA(String texto_a_cifrar, PublicKey clavePublica) throws Exception {
		
		// Cipher es una clase que nos sirve para cifrar y descifrar texto
		Cipher cifrador = Cipher.getInstance(RSA);
		
		// Con init iniciaremos la clase Cipher en Modo Encriptacion
		cifrador.init(Cipher.ENCRYPT_MODE, clavePublica);
		
		// Pasamos el texto a un array de bytes
		byte[] pasar_a_bytes = texto_a_cifrar.getBytes();
		
		// Con doFinal se encriptara el array de bytes que contiene los bytes del texto
		// lo que siginifica que encripta el texto
		byte[] encriptar = cifrador.doFinal(pasar_a_bytes);
		
		return encriptar;
		
	}

	// Debido a que en el concepto de cifrado asincrono una clave privada sirve tanto para cifrar como
	// para descifrar, se a optado por realizar una sobrecarga de metodos, solamente al metodo encriptacionRSA
	public static byte[] encriptacionRSA(String texto_a_cifrar, PrivateKey clavePrivada) throws Exception {
		
		// Cipher es una clase que nos sirve para cifrar y descifrar texto
		Cipher cifrador = Cipher.getInstance(RSA);
		
		// Con init iniciaremos la clase Cipher en Modo Encriptacion
		cifrador.init(Cipher.ENCRYPT_MODE, clavePrivada);
		
		// Pasamos el texto a un array de bytes
		byte[] pasar_a_bytes = texto_a_cifrar.getBytes();
		
		// Con doFinal se encriptara el array de bytes que contiene los bytes del texto
		// lo que siginifica que encripta el texto
		byte[] encriptar = cifrador.doFinal(pasar_a_bytes);
		
		return encriptar;
		
	}
	
	public static String desencriptacionRSA(byte[] texto_cifrado, PrivateKey clavePrivada) throws Exception {
		
		Cipher descifrador = Cipher.getInstance(RSA);
		
		// Con init iniciaremos la clase Cipher en Modo Desencriptacion
		descifrador.init(Cipher.DECRYPT_MODE, clavePrivada);
		
		// Con doFinal se desencriptara el array de bytes que contiene el texto,
		// lo que significa que desencriptara el texto
		byte[] texto_en_bytes = descifrador.doFinal(texto_cifrado);
		
		// Pasamos a texto el array de bytes resultante
		String mensaje_descifrado = new String(texto_en_bytes);
		
		return mensaje_descifrado;
		
	}
	
}
