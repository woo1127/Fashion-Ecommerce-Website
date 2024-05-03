<script>
	export let values = [];
	export let mandatory = false;
	export let multiple = false;

	function selectButton(val) {
		if (values.includes(val)) {
			if (!(mandatory && values.length === 1)) {
				values.splice(values.indexOf(val), 1);
				values = values
			}
		} else if (multiple) {
			values = [...values, val]
		} else {
			values = [val];
		}	
	}
</script>

<div>
	<slot {selectButton} {values} />
</div>