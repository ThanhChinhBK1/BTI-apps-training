# How to organize OpenAPI files

## `apps.yaml`

`apps.yaml` is the entrypoint for impulse-apps's OpenAPI definition.
In this file we define the following:

- API info
- Server url base path
- API tags
- Security schemes
- Paths: only reference to files which contains actual path object is defined here.
  The root `/` path object is here just for referencing the syntax.

## Referencing paths to actual path objects in other files.

- Let's say for the path `/projects` we reference to `./definitions/apps/projects.yaml#/paths/projects`
- The syntax for referencing here is called JSON pointer, more details about referencing here: [\$ref Syntax](https://swagger.io/docs/specification/using-ref/)
- So we must create a file that is `./definitions/apps/projects.yaml`
- This thing is NOT an OpenAPI file, just a normal YAML file that we use to store objects an import to our real `apps.yaml` OpenAPI file
- But nonetheless we will define the file with the same structure as an OpenAPI should, and that should be:

```yaml
components:
  schemas:
#    schemas are defined here
paths:
#  paths object are defined here
```

- Note that since this is NOT and OpenAPI file, we can't use actual path like `/projects` as the key for path objects, just remove the slashes and make it `projects`
- We can reference to other objects in the same file as we normally would
- For remote files, `./definitions/apps/projects.yaml#/paths/projects` means read the file `./definitions/apps/projects.yaml`, and reference to the path `paths/projects` in that file.
- Now we finally imported the path object to the actual OpenAPI file `apps.yaml`

## Some conventions

- For one YAML file, if there are more than 7 path objects, then (you don't have to, but) you should split it in someway to multiple files. Only the entrypoint file `apps.yaml` can have more than 7 path objects.
- In the "fake" OpenAPI files, we can simplify path objects key like this. Remove all the slashes from the real path and only take the last word, e.g.

```yaml
/datasets/{datasetId}/images/{imageId}/metadata:
  $ref: "./definitions/apps/datasets/images.yaml#/paths/metadata"
```

Notice the full path is `/datasets/{datasetId}/images/{imageId}/metadata`, but in the fake OpenAPI file, I only use `metadata` as the key for that path, this would help import it to the real OpenAPI file easier

## Appendix

More about organizing OpenAPI files here:
[Splitting specification file](http://apihandyman.io/writing-openapi-swagger-specification-tutorial-part-8-splitting-specification-file/)
