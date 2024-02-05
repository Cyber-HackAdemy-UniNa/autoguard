import '/auth/firebase_auth/auth_util.dart';
import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_toggle_icon.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/flutter_flow/upload_data.dart';
import 'add_car_widget.dart' show AddCarWidget;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class AddCarModel extends FlutterFlowModel<AddCarWidget> {
  ///  Local state fields for this page.

  FFUploadedFile? imageLocalVariable;

  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  final formKey = GlobalKey<FormState>();
  bool isDataUploading1 = false;
  FFUploadedFile uploadedLocalFile1 =
      FFUploadedFile(bytes: Uint8List.fromList([]));

  // State field(s) for model widget.
  FocusNode? modelFocusNode;
  TextEditingController? modelController;
  String? Function(BuildContext, String?)? modelControllerValidator;
  String? _modelControllerValidator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Field is required';
    }

    if (val.length < 2) {
      return 'Insert at least 2 characters';
    }
    if (val.length > 9) {
      return 'Characters limit exceeded';
    }
    if (!RegExp('^[a-zA-Z0-9 ]{2,9}\$').hasMatch(val)) {
      return 'Please enter only letters and numbers';
    }
    return null;
  }

  // State field(s) for plateNumber widget.
  FocusNode? plateNumberFocusNode;
  TextEditingController? plateNumberController;
  String? Function(BuildContext, String?)? plateNumberControllerValidator;
  String? _plateNumberControllerValidator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Field is required';
    }

    if (val.length < 4) {
      return 'Insert at least 4 characters';
    }
    if (val.length > 8) {
      return 'Characters limit exceeded';
    }
    if (!RegExp('^[a-zA-Z0-9]{4,8}\$').hasMatch(val)) {
      return 'Please enter only letters and numbers';
    }
    return null;
  }

  // State field(s) for vin widget.
  FocusNode? vinFocusNode;
  TextEditingController? vinController;
  String? Function(BuildContext, String?)? vinControllerValidator;
  String? _vinControllerValidator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Field is required';
    }

    if (val.length < 6) {
      return 'Insert at least 6 characters';
    }
    if (val.length > 16) {
      return 'Characters limit exceeded';
    }
    if (!RegExp('^[a-zA-Z0-9]{6,16}\$').hasMatch(val)) {
      return 'Please enter only letters and numbers';
    }
    return null;
  }

  bool isDataUploading2 = false;
  FFUploadedFile uploadedLocalFile2 =
      FFUploadedFile(bytes: Uint8List.fromList([]));

  // State field(s) for sharedSecretText widget.
  FocusNode? sharedSecretTextFocusNode;
  TextEditingController? sharedSecretTextController;
  String? Function(BuildContext, String?)? sharedSecretTextControllerValidator;
  // Stores action output result for [Backend Call - API (postNewVehicle)] action in Button widget.
  ApiCallResponse? responseApi;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {
    modelControllerValidator = _modelControllerValidator;
    plateNumberControllerValidator = _plateNumberControllerValidator;
    vinControllerValidator = _vinControllerValidator;
  }

  void dispose() {
    unfocusNode.dispose();
    modelFocusNode?.dispose();
    modelController?.dispose();

    plateNumberFocusNode?.dispose();
    plateNumberController?.dispose();

    vinFocusNode?.dispose();
    vinController?.dispose();

    sharedSecretTextFocusNode?.dispose();
    sharedSecretTextController?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
