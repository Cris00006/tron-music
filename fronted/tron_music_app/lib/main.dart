import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'config/api.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  Future<String> ping() async {
    final res = await http.get(Uri.parse('${ApiConfig.baseUrl}/ping'));
    return res.body;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: ElevatedButton(
            child: const Text('Ping backend'),
            onPressed: () async {
              final r = await ping();
              debugPrint(r);
            },
          ),
        ),
      ),
    );
  }
}

