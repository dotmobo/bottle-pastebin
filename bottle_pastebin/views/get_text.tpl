%include header

    <div class="container">

      <h1>Encrypt and share text with your friends</h1>
      
      <br />
      
      <div class="alert alert-info">
      	<strong>This link is valid until: </strong> {{ date_limit }}
      </div>
      
	  <textarea id="readtext" readonly="readonly" rows="15" class="field span12">{{ text_decrypted }}</textarea>
 
      
      
    </div> <!-- /container -->

%include footer