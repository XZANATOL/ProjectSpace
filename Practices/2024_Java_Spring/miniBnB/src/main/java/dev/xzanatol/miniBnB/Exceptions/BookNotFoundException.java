package dev.xzanatol.miniBnB.Exception;

public class BookNotFoundException extends RuntimeException {

    private final String errorCode;

    public BookNotFoundException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}