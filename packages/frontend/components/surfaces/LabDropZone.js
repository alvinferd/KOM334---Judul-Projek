import { Grid, Box, Button, Typography } from "@material-ui/core";
import { DropzoneArea } from "material-ui-dropzone";

import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  textField: {
    marginBottom: theme.spacing(2),
  },
}));

const ButtonSave = () => {
  return (
    <Grid container justify="flex-end">
      <Button variant="contained" color="primary">
        Simpan
      </Button>
    </Grid>
  );
};

const LabDropZone = ({ title, subtitle }) => {
  const classes = useStyles();
  return (
    <>
      <Box className={classes.textField}>
        <Typography variant="h4" component="div">
          {title}
        </Typography>
        <Typography component="div" color="textSecondary">
          {subtitle}
        </Typography>
        <Box mt={1.5}>
          <DropzoneArea />
        </Box>
      </Box>
      <ButtonSave />
    </>
  );
};

export default LabDropZone;
