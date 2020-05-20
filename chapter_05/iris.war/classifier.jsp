<%@ page import="java.io.*" %>
<%@ page import="org.apache.http.HttpResponse" %>
<%@ page import="org.apache.http.client.HttpClient" %>
<%@ page import="org.apache.http.client.methods.CloseableHttpResponse" %>
<%@ page import="org.apache.http.client.methods.HttpGet" %>
<%@ page import="org.apache.http.impl.client.CloseableHttpClient" %>
<%@ page import="org.apache.http.impl.client.DefaultHttpClient" %>
<%@ page import="org.apache.http.impl.client.HttpClients" %>

<%
	String pl = request.getParameter("pl");
	String pw = request.getParameter("pw");
	String sl = request.getParameter("sl");
	String sw = request.getParameter("sw");

	CloseableHttpClient client = HttpClients.createDefault();
	
	String url = "http://127.0.0.1:5000/classify";
	url = url + "/" + pl + "/" + pw + "/" + sl + "/" + sw;
	//4.5/1.5/5.4/3.0"; 
  System.out.println(url);

  HttpGet httpRequest = new HttpGet(url);

	CloseableHttpResponse httpResponse = null;
  try {
	  httpResponse = client.execute(httpRequest);
    int status = httpResponse.getStatusLine().getStatusCode();
    if (status >= 200 && status < 300) {
   		BufferedReader br;
        br = new BufferedReader(new InputStreamReader(
        	httpResponse.getEntity().getContent()));
        String data = "";	
        String line = "";
        while ((line = br.readLine()) != null) {
        	data = data + line;
       	}
       	out.print(data);
       	System.out.println(data);
   	} 
    else {
    	System.out.println("Unexpected response status: " + status);
  	}
  }         
  catch (IOException | UnsupportedOperationException e) {
  	e.printStackTrace();
 	} 
  finally {
    if(null != httpResponse){
      try {
       	httpResponse.close();
        client.close();
      } 
      catch (IOException e) {
        e.printStackTrace();
      }
    }
	}
%>
