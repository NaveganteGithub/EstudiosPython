package Src.pyJava.componentesJava;
// package Src.pyJava;
import java.math.BigInteger;
import gnu.crypto.hash.Haval;

public class cifradosHaval {
	/*
	 * 
	 * Fuente: https://www.bing.com/search?form=NTPCHB&q=Bing+AI&showconv=1
	 * 
	 * */
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
        // String mensaje = "hello";
		String mensaje = args[0];
		
		for (int ronda = 0; ronda < 3; ronda++)
			for (int bits = 0; bits < 5; bits++) {
				String[] cifrado = encriptarHaval(mensaje, bits, ronda);
				System.out.println("Haval" + cifrado[0] + "," + cifrado[1] + " " + cifrado[2]);
			}
		
		// System.out.println("\n" + encriptarTiger(mensaje));
	}
	
	public static byte[] codificacionBytes(String mensaje) {
		return mensaje.getBytes();
	}
	
	public static String codificacionHexadecimal(byte[] mensaje) {
		return new BigInteger(1, mensaje).toString(16);
	}
	
	public static String[] encriptarHaval(String mensaje, int bits, int ronda) {
		
		/*
		    Este es el enlace de la fuente original, pero no lo utilices, se sospecha que pueda tener implementado
		    un malware Chino con la ayuda de virustotal.com, y se ha tenido que realizar ciertas acciones para 
		    descargar la informe sin el malware.
	
		    https://web.archive.org/web/20050308141821/https://www.calyptix.com/files/haval-paper.pdf
	
		    https://www.virustotal.com/gui/url/5b134512fb654b3194799f2f901a0b508275bbae792a0029bc2ff9d93211ec5f/detection
	    */
		
		final int size[] = {Haval.HAVAL_128_BIT, Haval.HAVAL_160_BIT, Haval.HAVAL_192_BIT, Haval.HAVAL_224_BIT, Haval.HAVAL_256_BIT};
		final int round[] = {Haval.HAVAL_3_ROUND, Haval.HAVAL_4_ROUND, Haval.HAVAL_5_ROUND};
		final String[] tamanos_disponibles = {"128", "160", "192", "224", "256"};
		final String[] rondas_disponibles = {"3", "4", "5"};
		
		byte[] codificacion = codificacionBytes(mensaje);

		final Haval haval = new Haval(size[bits], round[ronda]);
		haval.update(codificacion, 0, codificacion.length);
		
		byte[] mensaje_cifrado = haval.digest();

		return new String[] {tamanos_disponibles[bits], rondas_disponibles[ronda], codificacionHexadecimal(mensaje_cifrado)};
		
	}
	
	/*public static String encriptarTiger(String mensaje) {
		
		Tiger tiger = new Tiger();
		byte[] codificacion = codificacionBytes(mensaje);
		tiger.update(codificacion, 0, codificacion.length);
		
		return codificacionHexadecimal(tiger.digest()); 
	}*/

}
