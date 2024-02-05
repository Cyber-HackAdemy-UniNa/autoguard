import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyD4zHn_wFQTQTF-NjPhses_2ulVzk_u7Vo",
            authDomain: "cyberhackademy-pw2023-group1.firebaseapp.com",
            projectId: "cyberhackademy-pw2023-group1",
            storageBucket: "cyberhackademy-pw2023-group1.appspot.com",
            messagingSenderId: "987502902667",
            appId: "1:987502902667:web:5b81ce991204703880438e"));
  } else {
    await Firebase.initializeApp();
  }
}
