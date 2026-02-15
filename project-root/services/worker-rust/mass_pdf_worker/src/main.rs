use rayon::prelude::*;
use walkdir::WalkDir;
use reqwest::blocking::Client;
use serde::Serialize;
use anyhow::Result;

#[derive(Serialize)]
struct PdfPayload {
    file_path: String,
}

const ETL_URL: &str = "http://localhost:8002/run-etl"; 
// ← este endpoint lo vamos a crear en Python en el siguiente paso

fn main() -> Result<()> {
    println!("🚀 Worker Rust – Procesamiento masivo de PDFs iniciado...\n");

    let client = Client::new();

    // Recorre la carpeta /pdfs/
    let pdf_paths: Vec<String> = WalkDir::new("./pdfs")
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.path().is_file())
        .filter(|e| e.path().extension().map(|ext| ext == "pdf").unwrap_or(false))
        .map(|e| e.path().display().to_string())
        .collect();

    println!("📄 Encontrados {} PDFs para procesar.\n", pdf_paths.len());

    pdf_paths.par_iter().for_each(|pdf| {
        println!("➡️ Procesando: {}", pdf);

        let payload = PdfPayload {
            file_path: pdf.to_string(),
        };

        let response = client.post(ETL_URL).json(&payload).send();

        match response {
            Ok(res) => {
                if res.status().is_success() {
                    println!("   ✔ Procesado correctamente\n");
                } else {
                    println!("   ❌ Error en ETL (HTTP {})\n", res.status());
                }
            }
            Err(err) => println!("   ❌ Error enviando al ETL: {}\n", err),
        }
    });

    println!("🏁 Procesamiento masivo completado.");
    Ok(())
}
