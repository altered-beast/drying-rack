// creates a statbox
function Statbox(props) {
  return (
    <div
      style="width : 80%; height: 20%; background-color : green;"
      id=""
      class="StatBox"
    >
      <textarea class="InnerStatBox" id="{ props.id }" contentEditable="true">
        12
      </textarea>
    </div>
  );
}
// creates a number of statboxes equal to quantity
function CreateStatboxes(props) {
  for (let i = 0; i < {props.quantity}; i++) {
    return <Statbox id="{i}" />;
  }
}

// creates a number of secondary statboxes equal to quantity
function CreatesecondaryStatboxes(props){
   
}
function Collumn(props) {

  return <div style="width:12.5%; background-color:red;  height:100%;" class= "Column" contentEditable="true">
    { props.content }
  </div>
  
}
