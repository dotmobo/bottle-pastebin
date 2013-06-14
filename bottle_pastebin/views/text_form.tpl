%include header

    <div class="container">

      <h1>Encrypt and share text with your friends</h1>
      
      <br />
      
      <div id="giveLink"></div>
      
      <form id="createForm" class="form-horizontal" method="POST" action="/create">
      
      	<div class="control-group">
      		<label class="control-label" for="inputValid">Choose a duration: </label>
      		<div class="controls">  
      			<select required="required" id="inputValid" name="inputValid">
      				%for row in valids:
      					<option value="{{ row }}">{{ valids[row] }}</option>
      				%end
      			</select>
      		</div>
      	</div>
      
      	<div class="control-group">
      		<label class="control-label" for="inputText">Enter your text: </label>
      		<div class="controls">
      			<textarea required="required" rows="15" class="field span10" id="inputText" name="inputText" placeholder="type here ..."></textarea>
      		</div>
      	</div>
      	
      	<div class="control-group">
      		<div class="controls">
      			<button type="submit" class="btn">Create</button>
      		</div>
      	</div>
      
      </form>
      
      
    </div> <!-- /container -->

%include footer
