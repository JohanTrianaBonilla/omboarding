use anyhow::Result;
use rayon::prelude::*;
use reqwest::blocking::Client;
use serde::Serialize;
use std::env;
use walkdir::WalkDir;

#[derive(Serialize)]
struct PdfPayload {
    file_path: String,
}

fn main() -> Result<()> {
    println!("Mass PDF worker iniciado");

    let client = Client::new();
    let fastapi_url = env::var("FASTAPI_URL").unwrap_or_else(|_| "http://api:8000".to_string());
    let etl_url = format!("{}/files/run-etl", fastapi_url.trim_end_matches('/'));

    let pdf_paths: Vec<String> = WalkDir::new("/pdfs")
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.path().is_file())
        .filter(|e| e.path().extension().map(|ext| ext == "pdf").unwrap_or(false))
        .map(|e| e.path().display().to_string())
        .collect();

    println!("Encontrados {} PDFs para procesar", pdf_paths.len());

    pdf_paths.par_iter().for_each(|pdf| {
        println!("Procesando {}", pdf);

        let payload = PdfPayload {
            file_path: pdf.to_string(),
        };

        let response = client.post(&etl_url).json(&payload).send();

        match response {
            Ok(res) => {
                if res.status().is_success() {
                    println!("Procesado correctamente");
                } else {
                    println!("Error en ETL (HTTP {})", res.status());
                }
            }
            Err(err) => println!("Error enviando al ETL: {}", err),
        }
    });

    println!("Procesamiento masivo completado");
    Ok(())
}
