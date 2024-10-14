package Src.pyJava.componentesJava;

import gnu.crypto.cipher.CipherFactory;
import gnu.crypto.cipher.DES;
import gnu.crypto.cipher.IBlockCipher;
import gnu.crypto.cipher.TripleDES;
import gnu.crypto.hash.HashFactory;
import gnu.crypto.hash.IMessageDigest;
import gnu.crypto.pad.IPad;
import gnu.crypto.pad.PadFactory;
import gnu.crypto.pad.WrongPaddingException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Array;
import java.security.InvalidKeyException;
import java.util.HashMap;
import java.util.HexFormat;
import java.util.Map;

/*
 * https://www.java-forum.org/thema/verwendung-der-cipher-von-gnu-crypto-serpent.137796/
 * https://www.cl.cam.ac.uk/%7Erja14/serpent.html
 * https://www.gnu.org/software/gnu-crypto/algorithms.html
 * https://en.wikipedia.org/wiki/Serpent_(cipher)#External_links
 * 
 * */

public class Encriptaciones {
	
	public static final String CIPHER_ANUBIS="anubis";
	public static final String CIPHER_BLOWFISH="blowfish";
	public static final String CIPHER_CAST5="cast5"; // Problema
	public static final String CIPHER_DES="des";
	public static final String CIPHER_KHAZAD="khazad"; // Problema
	public static final String CIPHER_RIJNDAEL="rijndael";
	public static final String CIPHER_SERPENT="serpent";
	public static final String CIPHER_SQUARE="square"; // Problema
	public static final String CIPHER_TRIPLEDES="tripledes";
	public static final String CIPHER_TWOFISH="twofish";
	
	public static final String[] CIPHERS = {"anubis", "blowfish", "cast5", "des", "khazad", 
											"rijndael", "serpent", "square", "tripledes", 
											"twofish"}; 
	
	public static final String HASH_HAVAL="haval";
	public static final String HASH_MD2="md2";
	public static final String HASH_MD4="md4";
	public static final String HASH_MD5="md5";
	public static final String HASH_RIPEMD128="ripemd128";
	public static final String HASH_SHA160="sha-160";
	public static final String HASH_SHA256="sha-256";
	public static final String HASH_SHA384="sha-384";
	public static final String HASH_SHA512="sha-512";
	public static final String HASH_TIGER="tiger";
	public static final String HASH_WHIRLPOOL="whirlpool";
	
	public static final String[] HASHES = {"haval", "md2", "md4", "md5", "ripemd128", 
											"sha-160", "sha-256", "sha-384", "sha-512", 
											"tiger", "whirlpool"};
	
	public static final String PAD_EME_PKCS1_v1_5="eme-pkcs1-v1.5";
	public static final String PAD_PKCS7="pkcs7";
	public static final String PAD_TBC="tbc";
	
	public static final String[] PADS = {"eme-pkcs1-v1.5", "pkcs7", "tbc"};
	
	private static String DEFAULT_CIPHER;
	private static String DEFAULT_HASH;
	private static String DEFAULT_PAD;
	private static final int DEFAULT_BUFFER_SIZE=1024;
	
	private Encriptaciones(){
	}

	public static void main(String[] args) {
		
		// short encriptacion = 6;
		short encriptacion = Short.valueOf(args[2]);
		
		switch (encriptacion) {
		case 3, 8: // Para ejecutar el codigo correspondiente a los algorimos DES y 3DES; 3 Posiciones de args: Mensaje, Clave, Encriptacion
			try {
				if (encriptacion == 3) {
					// encryptDES("I am text to be hidden away", "12345678");
					encryptDES(args[0], args[1]);
				} else {
					// encryptTripleDES("I am text to be hidden away", "123456781234567812345678");
					encryptTripleDES(args[0], args[1]);
				}
			} catch (InvalidKeyException | UnsupportedEncodingException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		case 2, 4, 7:
			System.out.println(encriptacion);
			break;
		default: // 5 Posiciones de args: Mensaje, Clave, Encriptacion, hash, pad
			// byte[] mensaje = "Hola".getBytes();
			// byte[] clave = "12345678".getBytes();
			
			byte[] mensaje = args[0].getBytes();
			byte[] clave = args[1].getBytes();
			
			// short modo_hash = 6;
			// short modo_PAD = 2;

			short modo_hash = Short.valueOf(args[3]);
			short modo_PAD = Short.valueOf(args[4]);

			DEFAULT_CIPHER = CIPHERS[encriptacion];
			DEFAULT_HASH = HASHES[modo_hash];
			DEFAULT_PAD = PADS[modo_PAD];
			
			try {
				byte[] texto_cifrado = encrypt(mensaje, clave);
				System.out.println(HexFormat.of().formatHex(texto_cifrado));
			} catch (InvalidKeyException | IllegalStateException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		}
		
		
	}
	
	public static byte[] encrypt(byte[] input, byte[] key) throws InvalidKeyException, IllegalStateException{
		return encrypt(input, key, DEFAULT_CIPHER, DEFAULT_HASH, DEFAULT_PAD);
	}
	
	public static void encrypt(InputStream inputStream, OutputStream outputStream, byte[] key) throws IOException, InvalidKeyException, IllegalStateException{
		encrypt(inputStream, outputStream, key, DEFAULT_BUFFER_SIZE, DEFAULT_CIPHER, DEFAULT_HASH, DEFAULT_PAD);
	}
	
	public static void encrypt(InputStream inputStream, OutputStream outputStream, byte[] key, int bufferSize, String cipherName, String hashName, String padName) throws InvalidKeyException, IllegalStateException, IOException{
		int read;
		byte[] buffer=new byte[bufferSize];
		while((read=inputStream.read(buffer))!=-1){
			byte[] temp=new byte[read];
			System.arraycopy(buffer, 0, temp, 0, read);
			outputStream.write(encrypt(temp, key));
		}
	}
	
	public static byte[] encrypt(byte[] input, byte[] key, String cipherName, String hashName, String padName) throws InvalidKeyException, IllegalStateException{
		IBlockCipher iBlockCipher=CipherFactory.getInstance(cipherName);
		int blockSize=iBlockCipher.defaultBlockSize();
		Map<String, Object> attributes=new HashMap<String, Object>();
		attributes.put(IBlockCipher.CIPHER_BLOCK_SIZE, blockSize);
		attributes.put(IBlockCipher.KEY_MATERIAL, getHash(key, hashName));
		iBlockCipher.init(attributes);
		byte[] paddedInput=getPaddedData(input, padName, blockSize);
		byte[] output=new byte[paddedInput.length];
		for(int i=0;i<paddedInput.length/blockSize;i++){
			iBlockCipher.encryptBlock(paddedInput, i*blockSize, output, i*blockSize);
		}
		return output;
	}
	
	public static byte[] getHash(byte[] input, String hashName){
		IMessageDigest iMessageDigest=HashFactory.getInstance(hashName);
		iMessageDigest.update(input, 0, input.length);
		return iMessageDigest.digest();
	}
	
	public static byte[] getPaddedData(byte[] input, String padName, int blockSize){
		IPad iPad=PadFactory.getInstance(padName);
		iPad.init(blockSize);
		byte[] padSequence=iPad.pad(input, 0, input.length);
		byte[] output=new byte[input.length+padSequence.length];
		System.arraycopy(input, 0, output, 0, input.length);
		System.arraycopy(padSequence, 0, output, input.length, padSequence.length);
		return output;
	}
	
	public static byte[] getUnpaddedData(byte[] input, String padName, int blockSize) throws WrongPaddingException{
		IPad iPad=PadFactory.getInstance(padName);
		iPad.init(blockSize);
		int remove=iPad.unpad(input, 0, input.length);
		byte[] output=new byte[input.length-remove];
		System.arraycopy(input, 0, output, 0, output.length);
		return output;
	}
	
	public static boolean compareHashes(byte[] input1, byte[] input2){
		if(input1.length!=input2.length){
			return false;
		}
		else{
			for(int i=0;i<input1.length;i++){
				if(input1[i]!=input2[i]){
					return false;
				}
			}
		}
		return true;
	}
	
	///////////////////////////////// METODOS INDEPENDIENTES ///////////////////////////////// 
	
	public static void encryptDES(String textInit, String key) throws InvalidKeyException, UnsupportedEncodingException {
		byte[] plainText;
		byte[] encryptedText;
		
		DES des = new DES();
		
		// create a key
		byte[] keyBytes = key.getBytes();
		Object keyObject = des.makeKey(keyBytes, 8);
		
		//make the length of the text a multiple of the block size
		if ((textInit.length() % 8) != 0) {
			while ((textInit.length() % 8) != 0) {
				textInit += " ";
			}
		}
		
		// initialize byte arrays for plain/encrypted text
		plainText = textInit.getBytes("UTF8");
		encryptedText = new byte[textInit.length()];
		
		// encrypt text in 8-byte chunks
		for (int i=0; i<Array.getLength(plainText); i+=8) {
			des.encrypt(plainText, i, encryptedText, i, keyObject, 8);
		}
		
		String encryptedString = Base64Coder.encodeLines(encryptedText);
		System.out.println(encryptedString);
	}
	
	public static void encryptTripleDES(String textInit, String key) throws InvalidKeyException, UnsupportedEncodingException {
		byte[] plainText;
		byte[] encryptedText;
		
		TripleDES des = new TripleDES();
		
		// create a key
		byte[] keyBytes = key.getBytes();
		Object keyObject = des.makeKey(keyBytes, 8);
		
		//make the length of the text a multiple of the block size
		if ((textInit.length() % 8) != 0) {
			while ((textInit.length() % 8) != 0) {
				textInit += " ";
			}
		}
		
		// initialize byte arrays for plain/encrypted text
		plainText = textInit.getBytes("UTF8");
		encryptedText = new byte[textInit.length()];
		
		// encrypt text in 8-byte chunks
		for (int i=0; i<Array.getLength(plainText); i+=8) {
			des.encrypt(plainText, i, encryptedText, i, keyObject, 8);
		}
		
		String encryptedString = Base64Coder.encodeLines(encryptedText);
		System.out.println(encryptedString);
	}

	///////////////////////////////// SUBCLASE Base64Coder /////////////////////////////////
	
	public class Base64Coder {
		// Copyright 2003-2010 Christian d'Heureuse, Inventec Informatik AG, Zurich, Switzerland
		// www.source-code.biz, www.inventec.ch/chdh
		//
		// This module is multi-licensed and may be used under the terms
		// of any of the following licenses:
		//
		//  EPL, Eclipse Public License, V1.0 or later, http://www.eclipse.org/legal
		//  LGPL, GNU Lesser General Public License, V2.1 or later, http://www.gnu.org/licenses/lgpl.html
		//  GPL, GNU General Public License, V2 or later, http://www.gnu.org/licenses/gpl.html
		//  AGPL, GNU Affero General Public License V3 or later, http://www.gnu.org/licenses/agpl.html
		//  AL, Apache License, V2.0 or later, http://www.apache.org/licenses
		//  BSD, BSD License, http://www.opensource.org/licenses/bsd-license.php
		//  MIT, MIT License, http://www.opensource.org/licenses/MIT
		//
		// Please contact the author if you need another license.
		// This module is provided "as is", without warranties of any kind.
		//
		// Project home page: www.source-code.biz/base64coder/java

		// The line separator string of the operating system.
		private static final String systemLineSeparator = System.getProperty("line.separator");

		// Mapping table from 6-bit nibbles to Base64 characters.
		private static final char[] map1 = new char[64];
		   static {
		      int i=0;
		      for (char c='A'; c<='Z'; c++) map1[i++] = c;
		      for (char c='a'; c<='z'; c++) map1[i++] = c;
		      for (char c='0'; c<='9'; c++) map1[i++] = c;
		      map1[i++] = '+'; map1[i++] = '/'; }

		// Mapping table from Base64 characters to 6-bit nibbles.
		private static final byte[] map2 = new byte[128];
		   static {
		      for (int i=0; i<map2.length; i++) map2[i] = -1;
		      for (int i=0; i<64; i++) map2[map1[i]] = (byte)i; }

		/**
		* Encodes a string into Base64 format.
		* No blanks or line breaks are inserted.
		* @param s  A String to be encoded.
		* @return   A String containing the Base64 encoded data.
		*/
		public static String encodeString (String s) {
			return new String(encode(s.getBytes())); 
		}

		/**
		* Encodes a byte array into Base 64 format and breaks the output into lines of 76 characters.
		* This method is compatible with <code>sun.misc.BASE64Encoder.encodeBuffer(byte[])</code>.
		* @param in  An array containing the data bytes to be encoded.
		* @return    A String containing the Base64 encoded data, broken into lines.
		*/
		public static String encodeLines (byte[] in) {
			return encodeLines(in, 0, in.length, 76, systemLineSeparator); 
		}

		/**
		* Encodes a byte array into Base 64 format and breaks the output into lines.
		* @param in            An array containing the data bytes to be encoded.
		* @param iOff          Offset of the first byte in <code>in</code> to be processed.
		* @param iLen          Number of bytes to be processed in <code>in</code>, starting at <code>iOff</code>.
		* @param lineLen       Line length for the output data. Should be a multiple of 4.
		* @param lineSeparator The line separator to be used to separate the output lines.
		* @return              A String containing the Base64 encoded data, broken into lines.
		*/
		public static String encodeLines (byte[] in, int iOff, int iLen, int lineLen, String lineSeparator) {
			
		   int blockLen = (lineLen*3) / 4;
		   if (blockLen <= 0) throw new IllegalArgumentException();
		   int lines = (iLen+blockLen-1) / blockLen;
		   int bufLen = ((iLen+2)/3)*4 + lines*lineSeparator.length();
		   StringBuilder buf = new StringBuilder(bufLen);
		   int ip = 0;
		   
		   while (ip < iLen) {
		      int l = Math.min(iLen-ip, blockLen);
		      buf.append(encode(in, iOff+ip, l));
		      buf.append(lineSeparator);
		      ip += l; }
		   return buf.toString(); 
		}

		/**
		* Encodes a byte array into Base64 format.
		* No blanks or line breaks are inserted in the output.
		* @param in  An array containing the data bytes to be encoded.
		* @return    A character array containing the Base64 encoded data.
		*/
		public static char[] encode (byte[] in) {
		   return encode(in, 0, in.length); 
		}

		/**
		* Encodes a byte array into Base64 format.
		* No blanks or line breaks are inserted in the output.
		* @param in    An array containing the data bytes to be encoded.
		* @param iLen  Number of bytes to process in <code>in</code>.
		* @return      A character array containing the Base64 encoded data.
		*/
		public static char[] encode (byte[] in, int iLen) {
		   return encode(in, 0, iLen); 
		}

		/**
		* Encodes a byte array into Base64 format.
		* No blanks or line breaks are inserted in the output.
		* @param in    An array containing the data bytes to be encoded.
		* @param iOff  Offset of the first byte in <code>in</code> to be processed.
		* @param iLen  Number of bytes to process in <code>in</code>, starting at <code>iOff</code>.
		* @return      A character array containing the Base64 encoded data.
		*/
		public static char[] encode (byte[] in, int iOff, int iLen) {
		   int oDataLen = (iLen*4+2)/3;       // output length without padding
		   int oLen = ((iLen+2)/3)*4;         // output length including padding
		   char[] out = new char[oLen];
		   int ip = iOff;
		   int iEnd = iOff + iLen;
		   int op = 0;
		   while (ip < iEnd) {
		      int i0 = in[ip++] & 0xff;
		      int i1 = ip < iEnd ? in[ip++] & 0xff : 0;
		      int i2 = ip < iEnd ? in[ip++] & 0xff : 0;
		      int o0 = i0 >>> 2;
		      int o1 = ((i0 &   3) << 4) | (i1 >>> 4);
		      int o2 = ((i1 & 0xf) << 2) | (i2 >>> 6);
		      int o3 = i2 & 0x3F;
		      out[op++] = map1[o0];
		      out[op++] = map1[o1];
		      out[op] = op < oDataLen ? map1[o2] : '='; op++;
		      out[op] = op < oDataLen ? map1[o3] : '='; op++; }
		   return out; 
		}

		/**
		* Decodes a string from Base64 format.
		* No blanks or line breaks are allowed within the Base64 encoded input data.
		* @param s  A Base64 String to be decoded.
		* @return   A String containing the decoded data.
		* @throws   IllegalArgumentException If the input is not valid Base64 encoded data.
		*/
		public static String decodeString (String s) {
			return new String(decode(s)); 
		}

		/**
		* Decodes a byte array from Base64 format and ignores line separators, tabs and blanks.
		* CR, LF, Tab and Space characters are ignored in the input data.
		* This method is compatible with <code>sun.misc.BASE64Decoder.decodeBuffer(String)</code>.
		* @param s  A Base64 String to be decoded.
		* @return   An array containing the decoded data bytes.
		* @throws   IllegalArgumentException If the input is not valid Base64 encoded data.
		*/
		public static byte[] decodeLines (String s) {
		   char[] buf = new char[s.length()];
		   int p = 0;
		   for (int ip = 0; ip < s.length(); ip++) {
		      char c = s.charAt(ip);
		      if (c != ' ' && c != '\r' && c != '\n' && c != '\t')
		         buf[p++] = c; }
		   return decode(buf, 0, p); 
		}

		/**
		* Decodes a byte array from Base64 format.
		* No blanks or line breaks are allowed within the Base64 encoded input data.
		* @param s  A Base64 String to be decoded.
		* @return   An array containing the decoded data bytes.
		* @throws   IllegalArgumentException If the input is not valid Base64 encoded data.
		*/
		public static byte[] decode (String s) {
			return decode(s.toCharArray()); 
		}

		/**
		* Decodes a byte array from Base64 format.
		* No blanks or line breaks are allowed within the Base64 encoded input data.
		* @param in  A character array containing the Base64 encoded data.
		* @return    An array containing the decoded data bytes.
		* @throws    IllegalArgumentException If the input is not valid Base64 encoded data.
		*/
		public static byte[] decode (char[] in) {
			return decode(in, 0, in.length); 
		}

		/**
		* Decodes a byte array from Base64 format.
		* No blanks or line breaks are allowed within the Base64 encoded input data.
		* @param in    A character array containing the Base64 encoded data.
		* @param iOff  Offset of the first character in <code>in</code> to be processed.
		* @param iLen  Number of characters to process in <code>in</code>, starting at <code>iOff</code>.
		* @return      An array containing the decoded data bytes.
		* @throws      IllegalArgumentException If the input is not valid Base64 encoded data.
		*/
		public static byte[] decode (char[] in, int iOff, int iLen) {
			
			if (iLen%4 != 0) throw new IllegalArgumentException("Length of Base64 encoded input string is not a multiple of 4.");
			
			while (iLen > 0 && in[iOff+iLen-1] == '=') iLen--;
			
			int oLen = (iLen*3) / 4;
			
			byte[] out = new byte[oLen];
			int ip = iOff;
			int iEnd = iOff + iLen;
			int op = 0;
			while (ip < iEnd) {
				int i0 = in[ip++];
				int i1 = in[ip++];
				int i2 = ip < iEnd ? in[ip++] : 'A';
				int i3 = ip < iEnd ? in[ip++] : 'A';
				if (i0 > 127 || i1 > 127 || i2 > 127 || i3 > 127)
					throw new IllegalArgumentException("Illegal character in Base64 encoded data.");
				int b0 = map2[i0];
				int b1 = map2[i1];
				int b2 = map2[i2];
				int b3 = map2[i3];
				if (b0 < 0 || b1 < 0 || b2 < 0 || b3 < 0)
					throw new IllegalArgumentException("Illegal character in Base64 encoded data.");
				int o0 = ( b0       <<2) | (b1>>>4);
				int o1 = ((b1 & 0xf)<<4) | (b2>>>2);
				int o2 = ((b2 &   3)<<6) |  b3;
				out[op++] = (byte)o0;
				if (op<oLen) out[op++] = (byte)o1;
				if (op<oLen) out[op++] = (byte)o2; 
			}
			
			return out;
			
		   }

			// Dummy constructor.
			private Base64Coder() {}

	} // end class Base64Coder
	
}
