const functions = require('firebase-functions');
const admin = require('firebase-admin');


// Testing Hello World
exports.helloWorld = functions.https.onRequest((req, res) => {
 res.send("Hello from Firebase!");
});

// Create member profile
exports.createProfile = functions.https.onRequest((req, res)  => {

	let email = req.body.email;
	let password = req.body.password;
	let photoURL = req.body.photoURL;
	let username = req.body.username;

	return admin.auth().createUser({
		email: email,
  		emailVerified: false,
  		password: password,
  		displayName: username,
  		photoURL: photoURL,
  		disabled: false
	}).then(function(userRecord) {

		var user = userRecord.toJSON();

		user['username'] = username;

		return admin.firestore().collection('profiles').doc(user.uid).set(user, {merge:true}).then(response => {
          return res.status(200).send(user);
        }).catch(error => {
          return res.status(500).send(user);
        });

	}).catch(function(error) {
	    return res.status(500).send(error)
	 });
});

// Upload a rating by a user 
exports.addStrainReview = functions.https.onRequest((req, res)  => {

	let userID = req.body.username;
	let strainID = req.body.strain_id;
	let ratingText = req.body.rating_text;
	let ratingNumber = req.body.rating_number;
	let lastName = req.body.last_name;

	return admin.auth().createUser({
	  email: email,
	  emailVerified: false,
	  username: username,
	  photoURL: photoURL,
	  firstName: firstName,
	  lastName: lastName,
	  disabled: false
	}).then(function(userRecord) {
		return res.status(200).send(userRecord)
	}).catch(function(error) {
	    return res.status(500).send(error)
	 });
});


// Upload a rating to a user 
exports.getAllUsers = functions.https.onRequest((req, res)  => {

	let userID = req.body.uid;
	let strainID = req.body.strain_id;
	let ratingText = req.body.rating_text;
	let ratingNumber = req.body.rating_number;
	let lastName = req.body.last_name;

	return admin.auth().createUser({
	  email: email,
	  emailVerified: false,
	  username: username,
	  photoURL: photoURL,
	  firstName: firstName,
	  lastName: lastName,
	  disabled: false
	}).then(function(userRecord) {
		return res.status(200).send(userRecord)
	}).catch(function(error) {
	    return res.status(500).send(error)
	 });
});





let citiesRef = db.collection('cities');
let query = citiesRef.where('capital', '==', true).get()
  .then(snapshot => {
    if (snapshot.empty) {
      console.log('No matching documents.');
      return;
    }  

    snapshot.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });
  })
  .catch(err => {
    console.log('Error getting documents', err);
  });

