/**
* This React class is intended to query an endpoint that will return an alphanumeric string, after clicking a button.
* This component is passed a prop "apiQueryDelay", which delays the endpoint request by N milliseconds. There is a 
* second button to disable this functionality and have the endpoint request run immediately after button click.
* This data is then to be displayed inside a simple container.
* The "queryAPI" XHR handler will return the endpoint response in the form of a Promise (such as axios, fetch).
* The response object will look like the following: {data: "A0B3HCJ"}
* The containing element ref isn't used, but should remain within the class.
* Please identify, correct and comment on any errors or bad practices you see in the React component class below.
* Additionally, please feel free to change the code style as you see fit.
* Please note - React version for this exercise is 15.5.4
*/

import React, { Component } from 'react';
import {queryAPI} from 'axios'; // import either fetch or axios 


class ShowResultsFromAPI extends Component {
  // the constructor of the super class Component takes in one parameter "props"

  // add the state of the component

  constructor(props) { // pass the props to the constructor
    super(props);
    this.state = {
      data: "xxxxxx", //default string
      error: false, //initialize to false
      apiQueryDelay: this.props.apiQueryDelay  //initialize the state to the props
    }
    this.container = null;
  }

  // add the event in this function
  onDisableDelay(e){
    // use state instead 
    this.setState({
      apiQueryDelay: 0
    });
    console.log("on disable");
  }

  // add the event paramenter
  click(e){
    console.log("on click");
    if (this.props.apiQueryDelay) {
      console.log("on click");
      setTimeout(function() {
        this.fetchData();
      }, this.state.apiQueryDelay);
    }
  }

  fetchData() {
    queryAPI()
      .then(function(response) {
        if (response.data) {
          this.setState({
            data: response.data,
            error: false
          });
        }
        
      });
  }

  render() {
    return (
          // put in a single div to cover everything
          <div>
              <div className="content-container" ref="container">
                {console.log(this.state)}
                {/* show date if error is false and the error me  */}
                <p>{!this.state.error ? this.state.data : "Sorry -  there was an error with your request."}</p>
               </div>
               <input type="submit" onClick={this.onDisableDelay.bind(this)} value="Disable request delay"/>
              <input type="submit" onClick={this.click.bind(this)} value="Request data from endpoint"/>
          </div>
    );
  }
}
// no need to set the name of the component since the it is thesame as the name of the class
/*ShowResultsFromAPI.displayName = {
  name: "ShowResultsFromAPI"
};*/

//  apiQueryDelay should be a state and not a property because it controled by this componentand not the parent
ShowResultsFromAPI.defaultProps = {
  apiQueryDelay: 0
};
// ShowResultsFromAPI.propTypes = {
//   apiQueryDelay: React.propTypes.number
// };

// export the right component class
export default ShowResultsFromAPI;