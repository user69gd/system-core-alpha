import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)
    println("--- Kotlin System Validator ---")
    
    val threshold = 100.0
    val systemValues = listOf(102.5, 405.0, 303.2, 908.1, 112.0)
    
    println("Verifying ${systemValues.size} critical values...")
    
    for (value in systemValues) {
        if (value > threshold) {
            println("  [VALID] Value $value exceeds safety threshold.")
        } else {
            println("  [ALERT] Value $value is below threshold!")
        }
    }
    
    println("\nValidation Process Finalized.")
}