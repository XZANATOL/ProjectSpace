import { ValidatorFn, AbstractControl, ValidationErrors } from "@angular/forms"

export function fileType(types: Array<string>): ValidatorFn{
	return (control: AbstractControl): ValidationErrors | null => {
		let valid = false
		types.forEach((type) => {
			const test = control.value.search(`\.${type}$`)
			if(test != -1){
				valid = true
			}
		})

		return (valid || control.value == "") ? null : {invalidType: {value: control.value}};
	}
}