package Src.pyJava.componentesJava;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HexFormat;

public class SHA3 {

	public static void main(String[] args) {
		
		String[] hashes = {"SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512"};
		
		for (String hash : hashes) {
			cifrado(args[0], hash);
		}
		
	}

	public static void cifrado(String texto, String tipoHash) {
		
		byte[] conversion = texto.getBytes();
			
			MessageDigest cifrado;
			String hexadecimal = "";
			
			try {
				
				cifrado = MessageDigest.getInstance(tipoHash);
			
				byte[] hash = cifrado.digest(conversion);
			
				hexadecimal = HexFormat.of().formatHex(hash);
				
			} catch (NoSuchAlgorithmException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			System.out.println(hexadecimal);
			
	}
	
}
